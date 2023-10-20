import { ChangeDetectorRef, Component } from '@angular/core';
import { MediaMatcher } from '@angular/cdk/layout';

@Component({
  selector: 'app-dashboard-cand',
  templateUrl: './dashboard-cand.component.html',
  styleUrls: ['./dashboard-cand.component.css']
})
export class DashboardCandComponent {
  mobileQuery: MediaQueryList;

  // fillerNav = Array.from({length: 50}, (_, i) => `Nav Item ${i + 1}`);
  fillerNav = [
    { name: 'Información Personal', route: '', icon: 'person' },
    { name: 'Información académica', route: 'info-academica', icon: 'school' },
    { name: 'Información técnica', route: '', icon: 'build' },
    { name: 'Información laboral', route: '', icon: 'work' },
    { name: 'Entrevistas pendientes', route: '', icon: 'assignment_late' },
    { name: 'Entrevistas realizadas', route: '', icon: 'assignment_turned_in' }
  ]

  private _mobileQueryListener: () => void;

  constructor(changeDetectorRef: ChangeDetectorRef, media: MediaMatcher) {
    this.mobileQuery = media.matchMedia('(max-width: 600px)');
    this._mobileQueryListener = () => changeDetectorRef.detectChanges();
    this.mobileQuery.addListener(this._mobileQueryListener);
  }

  ngOnDestroy(): void {
    this.mobileQuery.removeListener(this._mobileQueryListener);
  }
}
