# CardTypeCustomControl.SetVisible - метод
Устанавливает признак того, что элемент управления является видимым в
интерфейсе. Если элемент управления не поддерживает установку такого признака,
то действий не выполняется.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override CardTypeControl SetVisible(
    	bool visible
    )
VB __Копировать
     Public Overrides Function SetVisible ( 
    	visible As Boolean
    ) As CardTypeControl
C++ __Копировать
     public:
    virtual CardTypeControl^ SetVisible(
    	bool visible
    ) override
F# __Копировать
     abstract SetVisible : 
            visible : bool -> CardTypeControl 
    override SetVisible : 
            visible : bool -> CardTypeControl 
#### Параметры
visible [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
#### Возвращаемое значение
[CardTypeControl](T_Tessa_Cards_CardTypeControl.htm)  
Текущий объект для цепочки вызовов.
##  __См. также
#### Ссылки
[CardTypeCustomControl - ](T_Tessa_Cards_CardTypeCustomControl.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
