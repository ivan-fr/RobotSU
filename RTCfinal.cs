using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using System;
using System.Threading;
using System.Net.Sockets;
using System.Text;

[System.Serializable]
public class TerrainContinu
{
    public string __class;
    public double caseParUnite;
    public List<Polygone> listePolygone;
    public Polygone polygoneSurface;
}

[System.Serializable]
public class Polygone
{
    public string __class;
    public List<List<double>> liste_sommet;
    public List<Vecteur> liste_vecteur;
}

[System.Serializable]
public class Robot
{
    public string __class;
    public double angle;
    public bool lastCollision;
    public Vecteur vecteurDeplacement;
    public float x;
    public float y;
}

[System.Serializable]
public class Vecteur
{
    public string __class;
    public double x;
    public double y;
}

public class RTCfinal : MonoBehaviour
{
    // public GameObject robotSimu;
    public Transform tc;
    public Transform r;
    private Vector3 tailleTC;

    private TcpClient client;
    private NetworkStream stream;

    private Robot robot;

    private TerrainContinu repTC;

    private Byte[] data;
    private Byte[] dataSend = System.Text.Encoding.ASCII.GetBytes("pong");

    private void Connect(String server)
    {
        Int32 port = 65432;
        this.client = new TcpClient(server, port);
        this.stream = client.GetStream();
        stream.Write(this.dataSend, 0, this.dataSend.Length);
    }

    void Start()
    {
        Connect("127.0.0.1");
        this.data = new Byte[4096];
        String responseData = String.Empty;

        int bytes = stream.Read(this.data, 0, this.data.Length);
        responseData = System.Text.Encoding.ASCII.GetString(this.data, 0, bytes);
        Debug.Log(responseData);
        this.repTC = JsonUtility.FromJson<TerrainContinu>(responseData.ToString());
        Debug.Log(repTC.caseParUnite);
    }

    // Update is called once per frame
    void Update()
    {
        if (client == null)
        {
            return;
        }

        this.stream.Write(this.dataSend, 0, this.dataSend.Length);
        String responseData = String.Empty;
        int bytes = this.stream.Read(this.data, 0, this.data.Length);
        responseData = System.Text.Encoding.ASCII.GetString(this.data, 0, bytes);

        if (responseData == String.Empty)
        {
            return;
        }

        if (responseData == "ok")
        {
            stream.Close();
            client.Close();

            stream = null;
            client = null;

            return;
        }

        Debug.Log(responseData);
        robot = JsonUtility.FromJson<Robot>(responseData);

        //recuperer infos sur polygone surface de TC
        Polygone p = repTC.polygoneSurface;
        Debug.Log(p.liste_vecteur[1].x);
        Debug.Log(p.liste_vecteur[1].y);
        Debug.Log(p.liste_vecteur[2]);

        //on cree le robot represente par un carre
        Transform robotSimu = Instantiate(this.r, new Vector3(robot.x, 1, robot.y), transform.rotation);
        Renderer rend = robotSimu.GetComponent<Renderer>();
        rend.material = Resources.Load<Material>("blue");
        Transform TerrainCsimu = Instantiate(this.tc, transform.position, transform.rotation);
        float TCx = Convert.ToSingle(p.liste_vecteur[1].y);
        float TCz = Convert.ToSingle(p.liste_vecteur[0].x);
        tailleTC = new Vector3(TCx, 0, TCz);
        TerrainCsimu.transform.localScale = tailleTC;
    }
}

