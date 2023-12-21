# CardRow.NotifyFieldChanged - метод
Уведомляет подписчиков событий о том, что изменилось поле.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void NotifyFieldChanged(
    	string fieldName
    )
VB __Копировать
     Public Sub NotifyFieldChanged ( 
    	fieldName As String
    )
C++ __Копировать
     public:
    virtual void NotifyFieldChanged(
    	String^ fieldName
    ) sealed
F# __Копировать
     abstract NotifyFieldChanged : 
            fieldName : string -> unit 
    override NotifyFieldChanged : 
            fieldName : string -> unit 
#### Параметры
fieldName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя поля, об изменении которого уведомляются подписчики событий.
#### Реализации
[ICardFieldContainer.NotifyFieldChanged(String)](M_Tessa_Cards_ICardFieldContainer_NotifyFieldChanged.htm)  
##  __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
Параметр fieldName равен null.  
---|---  
##  __См. также
#### Ссылки
[CardRow - ](T_Tessa_Cards_CardRow.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
