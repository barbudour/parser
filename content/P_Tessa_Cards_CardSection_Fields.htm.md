# CardSection.Fields - свойство
Значения полей для строковой секции с поддержкой состояний. При изменении
значений любого поля через это свойство такое поле помечается как изменённое.
Если секция является коллекционной или древовидной, то при этом вызывается
исключение
[NotSupportedException](https://learn.microsoft.com/dotnet/api/system.notsupportedexception).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IDictionary<string, Object> Fields { get; }
VB __Копировать
     Public ReadOnly Property Fields As IDictionary(Of String, Object)
    	Get
C++ __Копировать
     public:
    virtual property IDictionary<String^, Object^>^ Fields {
    	IDictionary<String^, Object^>^ get () sealed;
    }
F# __Копировать
     abstract Fields : IDictionary<string, Object> with get
    override Fields : IDictionary<string, Object> with get
#### Значение свойства
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
#### Реализации
[ICardFieldContainer.Fields](P_Tessa_Cards_ICardFieldContainer_Fields.htm)  
##  __Исключения
[NotSupportedException](https://learn.microsoft.com/dotnet/api/system.notsupportedexception)|
Секция является коллекционной или древовидной.  
---|---  
##  __См. также
#### Ссылки
[CardSection - ](T_Tessa_Cards_CardSection.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
