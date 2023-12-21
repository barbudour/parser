# CardSection - конструктор
Создаёт экземпляр класса с указанием хранилища, декоратором для которого
является создаваемый объект.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardSection(
    	string name,
    	Dictionary<string, Object> storage
    )
VB __Копировать
     Public Sub New ( 
    	name As String,
    	storage As Dictionary(Of String, Object)
    )
C++ __Копировать
     public:
    CardSection(
    	String^ name, 
    	Dictionary<String^, Object^>^ storage
    )
F# __Копировать
     new : 
            name : string * 
            storage : Dictionary<string, Object> -> CardSection
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Название секции.
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, декоратором для которого является создаваемый объект.
##  __См. также
#### Ссылки
[CardSection - ](T_Tessa_Cards_CardSection.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
