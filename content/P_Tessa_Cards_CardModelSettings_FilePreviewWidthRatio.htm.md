# CardModelSettings.FilePreviewWidthRatio - свойство
Отношение ширины области предпросмотра к суммарной ширине области карточки и
области предпросмотра. Значение должно располагаться на отрезке [0;1].
Значение 0.5 означает, что области распределены в равных долях, а значение
0.25 определяет, что ширина области предпросмотра в три раза меньше, чем
область карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public double FilePreviewWidthRatio { get; }
VB __Копировать
     Public ReadOnly Property FilePreviewWidthRatio As Double
    	Get
C++ __Копировать
     public:
    virtual property double FilePreviewWidthRatio {
    	double get () sealed;
    }
F# __Копировать
     abstract FilePreviewWidthRatio : float with get
    override FilePreviewWidthRatio : float with get
#### Значение свойства
[Double](https://learn.microsoft.com/dotnet/api/system.double)
#### Реализации
[ICardModelSettings.FilePreviewWidthRatio](P_Tessa_Cards_ICardModelSettings_FilePreviewWidthRatio.htm)  
##  __См. также
#### Ссылки
[CardModelSettings - ](T_Tessa_Cards_CardModelSettings.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
