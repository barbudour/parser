# CardMetadataColumn.DefaultValue - свойство
Значение колонки по умолчанию, которое может быть размещено в карточке.
Определяется типом данных или значением, заданным в схеме. Для комплексной
колонки всегда возвращается null.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Object DefaultValue { get; set; }
VB __Копировать
     Public Property DefaultValue As Object
    	Get
    	Set
C++ __Копировать
     public:
    property Object^ DefaultValue {
    	Object^ get ();
    	void set (Object^ value);
    }
F# __Копировать
     member DefaultValue : Object with get, set
#### Значение свойства
[Object](https://learn.microsoft.com/dotnet/api/system.object)
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardMetadataColumn - ](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
[Tessa.Platform.ObjectSealedException]
