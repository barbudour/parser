# CardMetadataSection.IsVirtual - свойство
Получает или задаёт признак того, что секция является виртуальной. Значение
поля определяется флагом Virtual.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool IsVirtual { get; set; }
VB __Копировать
     Public Property IsVirtual As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    property bool IsVirtual {
    	bool get ();
    	void set (bool value);
    }
F# __Копировать
     member IsVirtual : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardMetadataSection - ](T_Tessa_Cards_Metadata_CardMetadataSection.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
[Tessa.Platform.ObjectSealedException]
