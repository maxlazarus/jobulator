using System;
using System.IO;
using System.Text.RegularExpressions;

namespace jobulator {
	public class FileHandler {

		public readonly static string slash = "", resPath = "", basePath = "";

		static FileHandler (){
			var os = System.Environment.OSVersion;
			slash = (os.ToString().Contains("Windows"))? "\\": "/";
			basePath = ".." + slash + ".." + slash;
			resPath = basePath + "res" + slash;
		}
		public static StreamReader Open (String s) {
			try {
				return new StreamReader(resPath + s);
			} catch {
				return null;
			}
		}
		public static string OpenAsString (String s) {
			var dir = (s.Contains("html"))? "jobs" + slash: "res" + slash;
			StreamReader sr = new StreamReader(basePath + dir + s);
			string line = "", document = "";
			while ((line = sr.ReadLine ()) != null) {
				document += line;
			}
			sr.Close ();
			return document;
		}
		public static void Write (string s, string name) {
			using (StreamWriter writer =
				new StreamWriter(resPath + name)) {
				writer.Write(s);
			}
		}
		public static System.Collections.Generic.List<string> getFileNames(string extension) {
			var dir = (extension.Contains ("html")) ? "jobs" + slash : "res" + slash;
			var filePaths = Directory.EnumerateFiles (basePath + dir, "*." + extension);
			return new System.Collections.Generic.List<string>(filePaths);
		}
	}
}

