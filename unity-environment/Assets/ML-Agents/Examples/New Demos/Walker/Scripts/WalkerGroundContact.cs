using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WalkerGroundContact : MonoBehaviour {

    public int index;
    public WalkerAgent agent;
    public bool touchingGround;
    // WalkerAgentMotorJoints agent;

    void Start(){
        // agent = transform.root.GetComponent<WalkerAgentMotorJoints>();
        agent = transform.root.GetComponent<WalkerAgent>();
    }

    // void OnCollisionStay(Collision other){
    //     if (other.transform.CompareTag("ground"))
    //     {
    //         agent.leg_touching[index] = true;
    //     }
    // }
    void OnCollisionEnter(Collision other){
        if (other.transform.CompareTag("ground"))
        {
            agent.leg_touching[index] = true;
            touchingGround = true;
        }
    }
    void OnCollisionExit(Collision other){
        if (other.transform.CompareTag("ground"))
        {
            agent.leg_touching[index] = false;
            touchingGround = false;
        }
    }

}
