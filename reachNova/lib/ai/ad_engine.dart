import 'ad_model.dart';

class AdEngine {
  static List<AdModel> getAdsByAge(int age) {
    if (age < 18) {
      return [
        AdModel(
          id: "A1",
          title: "Gaming Tournament",
          description: "Join youth gaming events",
        ),
        AdModel(
          id: "A2",
          title: "Student Learning App",
          description: "Free courses for students",
        ),
      ];
    } else if (age < 30) {
      return [
        AdModel(
          id: "A3",
          title: "Tech Gadgets Sale",
          description: "Latest laptops & mobiles",
        ),
        AdModel(
          id: "A4",
          title: "Internship Program",
          description: "Apply for paid internships",
        ),
      ];
    } else {
      return [
        AdModel(
          id: "A5",
          title: "Health Insurance",
          description: "Secure your future today",
        ),
        AdModel(
          id: "A6",
          title: "Investment Plans",
          description: "Smart investment solutions",
        ),
      ];
    }
  }
}
