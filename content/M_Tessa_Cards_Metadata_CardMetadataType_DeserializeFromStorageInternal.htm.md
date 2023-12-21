# CardMetadataType.DeserializeFromStorageInternal - метод
Выполняет десериализацию объекта и всех его дочерних объектов из хранилища
Dictionary<string, object>.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override void DeserializeFromStorageInternal(
    	Dictionary<string, Object> storage
    )
VB __Копировать
     Protected Overrides Sub DeserializeFromStorageInternal ( 
    	storage As Dictionary(Of String, Object)
    )
C++ __Копировать
     protected:
    virtual void DeserializeFromStorageInternal(
    	Dictionary<String^, Object^>^ storage
    ) override
F# __Копировать
     abstract DeserializeFromStorageInternal : 
            storage : Dictionary<string, Object> -> unit 
    override DeserializeFromStorageInternal : 
            storage : Dictionary<string, Object> -> unit 
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, в котором содержатся сериализованные данные.
##  __См. также
#### Ссылки
[CardMetadataType - ](T_Tessa_Cards_Metadata_CardMetadataType.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
