import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UpdateLivroComponent } from './update-livro.component';

describe('UpdateLivroComponent', () => {
  let component: UpdateLivroComponent;
  let fixture: ComponentFixture<UpdateLivroComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ UpdateLivroComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(UpdateLivroComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
