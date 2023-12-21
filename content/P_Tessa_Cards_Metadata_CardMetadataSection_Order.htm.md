# CardMetadataSection.Order - свойство
Номер, определяющий порядок сортировки секций при вставке данных в секции. При
удалении данных из секций порядок обратный.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public int Order { get; set; }
VB __Копировать
     Public Property Order As Integer
    	Get
    	Set
C++ __Копировать
     public:
    virtual property int Order {
    	int get () sealed;
    	void set (int value) sealed;
    }
F# __Копировать
     abstract Order : int with get, set
    override Order : int with get, set
#### Значение свойства
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)
#### Реализации
[ICardMetadataOrderable.Order](P_Tessa_Cards_ICardMetadataOrderable_Order.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardMetadataSection - ](T_Tessa_Cards_Metadata_CardMetadataSection.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
[Tessa.Platform.ObjectSealedException]
