# ICardModelSettings.ContentWidthRatio - свойство
Отношение ширины области карточки (вместе с заданиями) к суммарной ширине
области редактора карточки. Значение должно располагаться на отрезке [0;1].
Значение 1 означает, что карточка занимает всё доступное пространство без
пустой области справа. Значение 0.5 означает, что карточка занимает половину
доступной ширины, а значение 0.25 определяет, что ширина области карточки в
три раза меньше, чем пустая область справа.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     double ContentWidthRatio { get; }
VB __Копировать
     ReadOnly Property ContentWidthRatio As Double
    	Get
C++ __Копировать
    property double ContentWidthRatio {
    	double get ();
    }
F# __Копировать
     abstract ContentWidthRatio : float with get
#### Значение свойства
[Double](https://learn.microsoft.com/dotnet/api/system.double)
##  __См. также
#### Ссылки
[ICardModelSettings - ](T_Tessa_Cards_ICardModelSettings.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
