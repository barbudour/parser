# CardMetadataColumn.CardTypeIDList - свойство
Список идентификаторов типов карточек, в которых используется колонка.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public SealableList<Guid> CardTypeIDList { get; set; }
VB __Копировать
     Public Property CardTypeIDList As SealableList(Of Guid)
    	Get
    	Set
C++ __Копировать
     public:
    property SealableList<Guid>^ CardTypeIDList {
    	SealableList<Guid>^ get ();
    	void set (SealableList<Guid>^ value);
    }
F# __Копировать
     member CardTypeIDList : SealableList<Guid> with get, set
#### Значение свойства
[SealableList](T_Tessa_Platform_Collections_SealableList_1.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
##  __Заметки
Значение свойства никогда не равно null.
## __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardMetadataColumn - ](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
[Tessa.Platform.ObjectSealedException]
