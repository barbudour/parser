# CardCachedMetadata.HasData - свойство
Признак того, что кэш содержит данные. Если значение равно false, то кэш ещё
не заполнен или сброшен, поэтому обращение к другим его свойствам приведёт к
наполнению метаинформации.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool HasData { get; }
VB __Копировать
     Public ReadOnly Property HasData As Boolean
    	Get
C++ __Копировать
     public:
    virtual property bool HasData {
    	bool get () sealed;
    }
F# __Копировать
     abstract HasData : bool with get
    override HasData : bool with get
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
#### Реализации
[ICardCachedMetadata.HasData](P_Tessa_Cards_ICardCachedMetadata_HasData.htm)  
##  __См. также
#### Ссылки
[CardCachedMetadata - ](T_Tessa_Cards_Metadata_CardCachedMetadata.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
