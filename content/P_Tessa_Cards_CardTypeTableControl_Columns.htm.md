# CardTypeTableControl.Columns - свойство
Объекты, описывающие информацию о колонках коллекционных или древовидных
секций карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public SealableObjectList<CardTypeColumn> Columns { get; set; }
VB __Копировать
     Public Property Columns As SealableObjectList(Of CardTypeColumn)
    	Get
    	Set
C++ __Копировать
     public:
    property SealableObjectList<CardTypeColumn^>^ Columns {
    	SealableObjectList<CardTypeColumn^>^ get ();
    	void set (SealableObjectList<CardTypeColumn^>^ value);
    }
F# __Копировать
     member Columns : SealableObjectList<CardTypeColumn> with get, set
#### Значение свойства
[SealableObjectList](T_Tessa_Platform_Collections_SealableObjectList_1.htm)<[CardTypeColumn](T_Tessa_Cards_CardTypeColumn.htm)>
##  __Заметки
Значение свойства никогда не равно null.
## __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardTypeTableControl - ](T_Tessa_Cards_CardTypeTableControl.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
