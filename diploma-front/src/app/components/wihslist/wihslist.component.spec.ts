import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WihslistComponent } from './wihslist.component';

describe('WihslistComponent', () => {
  let component: WihslistComponent;
  let fixture: ComponentFixture<WihslistComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ WihslistComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(WihslistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
