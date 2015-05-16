using System;

namespace to_delete {
	public class Todo {
		public String Title {get; set;}
		public bool Complete {get; set;}
		public Todo(String title = "New Task") {
			Title = title;
			Complete = false;
		}

		public override String ToString() {
			return String.Format("{0} is {1}complete", Title, Complete ? "" : "not ");
		}

		public bool IsComplete() {
			return Complete;
		}

		public void Mark() {
			return Complete = true
			
		}
	}
}