# CardSerializableObject.DeserializeGuidListFromStorage - метод
Выполняет десериализацию заданного объекта SealableList<Guid> из хранилища
Dictionary<string, object>.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static void DeserializeGuidListFromStorage(
    	[NotNullAttribute] Dictionary<string, Object> storage,
    	[NotNullAttribute] string key,
    	[CanBeNullAttribute] ref SealableList<Guid> list
    )
VB __Копировать
     Protected Shared Sub DeserializeGuidListFromStorage ( 
    	<NotNullAttribute> storage As Dictionary(Of String, Object),
    	<NotNullAttribute> key As String,
    	<CanBeNullAttribute> ByRef list As SealableList(Of Guid)
    )
C++ __Копировать
     protected:
    static void DeserializeGuidListFromStorage(
    	[NotNullAttribute] Dictionary<String^, Object^>^ storage, 
    	[NotNullAttribute] String^ key, 
    	[CanBeNullAttribute] SealableList<Guid>^% list
    )
F# __Копировать
     static member DeserializeGuidListFromStorage : 
            [<NotNullAttribute>] storage : Dictionary<string, Object> * 
            [<NotNullAttribute>] key : string * 
            [<CanBeNullAttribute>] list : SealableList<Guid> byref -> unit 
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, содержащее сериализованные данные.
key [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ключ, по которому сериализованные данные расположены в хранилище storage. 
list
[SealableList](T_Tessa_Platform_Collections_SealableList_1.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Десериализуемый объект. Может быть равен null.
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
