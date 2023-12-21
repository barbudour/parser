# CardMetadataRecord.Item - свойство
Получает или задаёт значение поля в строке по имени колонки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Object this[
    	string columnName
    ] { get; set; }
VB __Копировать
     Public Default Property Item ( 
    	columnName As String
    ) As Object
    	Get
    	Set
C++ __Копировать
     public:
    property Object^ default[String^ columnName] {
    	Object^ get (String^ columnName);
    	void set (String^ columnName, Object^ value);
    }
F# __Копировать
     member Item : Object with get, set
#### Параметры
columnName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя колонки, по которому задаётся значение.
#### Возвращаемое значение
[Object](https://learn.microsoft.com/dotnet/api/system.object)  
Значение поля в строке.
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardMetadataRecord - ](T_Tessa_Cards_Metadata_CardMetadataRecord.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
[Tessa.Platform.ObjectSealedException]
