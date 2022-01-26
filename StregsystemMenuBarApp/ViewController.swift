//
//  ViewController.swift
//  StregsystemMenuBarApp
//
//  Created by Alexander Steffensen on 09/12/2021.
//

import Cocoa
import Foundation

class ViewController: NSViewController {
    @IBOutlet weak var product: NSPopUpButton!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override var representedObject: Any? {
        didSet {
        // Update the view, if already loaded.
        }
    }

    @IBAction func productChanged(_ sender: Any) {
    }
    
    @IBAction func buyProduct(_ sender: Any) {
    }
    
    
    @IBAction func updateBalance(_ sender: Any) {
        let dollars = executeCommand("python -u TheMindFrom99 -b")
        let errorMessage = "Noget gik galt 403"
        
        if (dollars == errorMessage){
        
        }
        else {
            syste
        }
        
        
        
    }
    
    func executeCommand(_ command: String) -> String{
        let task = Process()
        let pipe = Pipe()
        
        task.standardOutput = pipe
        task.standardError = pipe
        task.arguments = ["-c", command]
        task.launchPath = "~/repositories/stregsystem-cli"
        task.launch()
        
        let data = pipe.fileHandleForReading.readDataToEndOfFile()
        let output = String(data: data, encoding: .utf8)!
        
        return output
    }
    
}

