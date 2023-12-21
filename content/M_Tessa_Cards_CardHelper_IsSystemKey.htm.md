# CardHelper.IsSystemKey - метод
Определяет, является ли заданный ключ хранилища IDictionary<string, object>
системным ключом.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool IsSystemKey(
    	string key
    )
VB __Копировать
     Public Shared Function IsSystemKey ( 
    	key As String
    ) As Boolean
C++ __Копировать
     public:
    static bool IsSystemKey(
    	String^ key
    )
F# __Копировать
     static member IsSystemKey : 
            key : string -> bool 
#### Параметры
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ, для которого требуется определить, является ли он системным ключом.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если заданный ключ является системным ключом; false в противном случае.
## __Заметки
Системный ключ используется платформой и содержит служебную информацию.
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
