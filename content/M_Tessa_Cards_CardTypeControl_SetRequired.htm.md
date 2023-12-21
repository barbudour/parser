# CardTypeControl.SetRequired - метод
Устанавливает признак того, что значение, редактируемое элементом управления,
является обязательным для заполнения. Если элемент управления не поддерживает
установку такого признака, то действий не выполняется.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract CardTypeControl SetRequired(
    	bool required
    )
VB __Копировать
     Public MustOverride Function SetRequired ( 
    	required As Boolean
    ) As CardTypeControl
C++ __Копировать
     public:
    virtual CardTypeControl^ SetRequired(
    	bool required
    ) abstract
F# __Копировать
     abstract SetRequired : 
            required : bool -> CardTypeControl 
#### Параметры
required [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Признак того, что значение, редактируемое элементом управления, является обязательным для заполнения. 
#### Возвращаемое значение
[CardTypeControl](T_Tessa_Cards_CardTypeControl.htm)  
Текущий объект для цепочки вызовов.
##  __См. также
#### Ссылки
[CardTypeControl - ](T_Tessa_Cards_CardTypeControl.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
