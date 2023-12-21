# CardControlType - конструктор
Создаёт экземпляр типа с указанием идентификатора и имени типа элемента
управления.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardControlType(
    	Guid id,
    	string name,
    	CardControlTypeUsageMode usageMode,
    	CardControlTypeFlags flags
    )
VB __Копировать
     Public Sub New ( 
    	id As Guid,
    	name As String,
    	usageMode As CardControlTypeUsageMode,
    	flags As CardControlTypeFlags
    )
C++ __Копировать
     public:
    CardControlType(
    	Guid id, 
    	String^ name, 
    	CardControlTypeUsageMode usageMode, 
    	CardControlTypeFlags flags
    )
F# __Копировать
     new : 
            id : Guid * 
            name : string * 
            usageMode : CardControlTypeUsageMode * 
            flags : CardControlTypeFlags -> CardControlType
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа элемента управления.
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя типа элемента управления.
usageMode
[CardControlTypeUsageMode](T_Tessa_Cards_CardControlTypeUsageMode.htm)
    Способ использования элемента управления.
flags [CardControlTypeFlags](T_Tessa_Cards_CardControlTypeFlags.htm)
    Флаги элемента управления, описывающие его поведение.
##  __См. также
#### Ссылки
[CardControlType - ](T_Tessa_Cards_CardControlType.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
