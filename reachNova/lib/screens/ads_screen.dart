import 'package:flutter/material.dart';
import '../ai/ad_engine.dart';
import '../ai/click_tracker.dart';
import '../ai/ad_model.dart';

class AdsScreen extends StatelessWidget {
  final int userAge;

  const AdsScreen({super.key, required this.userAge});

  @override
  Widget build(BuildContext context) {
    List<AdModel> ads = AdEngine.getAdsByAge(userAge);

    return Scaffold(
      appBar: AppBar(title: const Text("Recommended Ads")),
      body: ListView.builder(
        itemCount: ads.length,
        itemBuilder: (context, index) {
          final ad = ads[index];
          return Card(
            child: ListTile(
              title: Text(ad.title),
              subtitle: Text(ad.description),
              trailing: const Icon(Icons.ads_click),
              onTap: () {
                ClickTracker.registerClick(ad.id);
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(
                    content: Text(
                      "Clicked ${ad.title} | Total clicks: ${ClickTracker.getClicks(ad.id)}",
                    ),
                  ),
                );
              },
            ),
          );
        },
      ),
    );
  }
}
