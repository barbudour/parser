# CardType.SchemeItems - свойство
Метаданные всех секций, входящих в состав типа карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public SealableObjectList<CardTypeSchemeItem> SchemeItems { get; set; }
VB __Копировать
     Public Property SchemeItems As SealableObjectList(Of CardTypeSchemeItem)
    	Get
    	Set
C++ __Копировать
     public:
    property SealableObjectList<CardTypeSchemeItem^>^ SchemeItems {
    	SealableObjectList<CardTypeSchemeItem^>^ get ();
    	void set (SealableObjectList<CardTypeSchemeItem^>^ value);
    }
F# __Копировать
     member SchemeItems : SealableObjectList<CardTypeSchemeItem> with get, set
#### Значение свойства
[SealableObjectList](T_Tessa_Platform_Collections_SealableObjectList_1.htm)<[CardTypeSchemeItem](T_Tessa_Cards_CardTypeSchemeItem.htm)>
##  __Заметки
Значение свойства никогда не равно null.
## __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardType - ](T_Tessa_Cards_CardType.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
