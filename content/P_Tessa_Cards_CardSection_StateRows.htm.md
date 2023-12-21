# CardSection.StateRows - свойство
Доступный только для чтения список значений полей для строк коллекционных и
древовидных секций с поддержкой состояний. При изменении значений любого поля
некоторой строки через это свойство такое поле и строка помечаются как
изменённые. Если секция является строковой, то вызывается исключение
[NotSupportedException](https://learn.microsoft.com/dotnet/api/system.notsupportedexception).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IList<IDictionary<string, Object>> StateRows { get; }
VB __Копировать
     Public ReadOnly Property StateRows As IList(Of IDictionary(Of String, Object))
    	Get
C++ __Копировать
     public:
    property IList<IDictionary<String^, Object^>^>^ StateRows {
    	IList<IDictionary<String^, Object^>^>^ get ();
    }
F# __Копировать
     member StateRows : IList<IDictionary<string, Object>> with get
#### Значение свойства
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>>
##  __Исключения
[NotSupportedException](https://learn.microsoft.com/dotnet/api/system.notsupportedexception)|
Секция является строковой.  
---|---  
##  __См. также
#### Ссылки
[CardSection - ](T_Tessa_Cards_CardSection.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
