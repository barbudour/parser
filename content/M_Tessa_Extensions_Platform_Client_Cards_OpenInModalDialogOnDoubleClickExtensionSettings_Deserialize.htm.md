# OpenInModalDialogOnDoubleClickExtensionSettings.Deserialize - метод
Выполняет десериализацию полей объекта из заданного хранилища.
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Cards](N_Tessa_Extensions_Platform_Client_Cards.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public Object Deserialize(
    	Dictionary<string, Object> storage
    )
VB __Копировать
     Public Function Deserialize ( 
    	storage As Dictionary(Of String, Object)
    ) As Object
C++ __Копировать
     public:
    virtual Object^ Deserialize(
    	Dictionary<String^, Object^>^ storage
    ) sealed
F# __Копировать
     abstract Deserialize : 
            storage : Dictionary<string, Object> -> Object 
    override Deserialize : 
            storage : Dictionary<string, Object> -> Object 
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, из которого десериализуется объект.
#### Возвращаемое значение
[Object](https://learn.microsoft.com/dotnet/api/system.object)  
Десериализованный объект.
#### Реализации
[IStorageSerializable.Deserialize(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_IStorageSerializable_Deserialize.htm)  
##  __См. также
#### Ссылки
[OpenInModalDialogOnDoubleClickExtensionSettings -
](T_Tessa_Extensions_Platform_Client_Cards_OpenInModalDialogOnDoubleClickExtensionSettings.htm)
[Tessa.Extensions.Platform.Client.Cards - пространство
имён](N_Tessa_Extensions_Platform_Client_Cards.htm)
