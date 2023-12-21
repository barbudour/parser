# CardSerializableObject.DeserializeObjectListFromStorageWithMaterialization -
метод
Выполняет десериализацию коллекции объектов
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) из
хранилища Dictionary<string, object>.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static void DeserializeObjectListFromStorageWithMaterialization(
    	[NotNullAttribute] Dictionary<string, Object> storage,
    	[NotNullAttribute] string key,
    	[NotNullAttribute] Action<CardSerializableObject> addItem,
    	ICardSerializableContext context
    )
VB __Копировать
     Protected Shared Sub DeserializeObjectListFromStorageWithMaterialization ( 
    	<NotNullAttribute> storage As Dictionary(Of String, Object),
    	<NotNullAttribute> key As String,
    	<NotNullAttribute> addItem As Action(Of CardSerializableObject),
    	context As ICardSerializableContext
    )
C++ __Копировать
     protected:
    static void DeserializeObjectListFromStorageWithMaterialization(
    	[NotNullAttribute] Dictionary<String^, Object^>^ storage, 
    	[NotNullAttribute] String^ key, 
    	[NotNullAttribute] Action<CardSerializableObject^>^ addItem, 
    	ICardSerializableContext^ context
    )
F# __Копировать
     static member DeserializeObjectListFromStorageWithMaterialization : 
            [<NotNullAttribute>] storage : Dictionary<string, Object> * 
            [<NotNullAttribute>] key : string * 
            [<NotNullAttribute>] addItem : Action<CardSerializableObject> * 
            context : ICardSerializableContext -> unit 
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, содержащее сериализованные данные.
key [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ключ, по которому сериализованные данные расположены в хранилище storage. 
addItem
[Action](https://learn.microsoft.com/dotnet/api/system.action-1)<[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm)>
     Метод, вызываемый для каждого десериализованного объекта, чтобы добавить его в некоторую коллекцию. 
context [ICardSerializableContext](T_Tessa_Cards_ICardSerializableContext.htm)
    Контекст, содержащий информацию по сериализации об объекте [CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm).
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
