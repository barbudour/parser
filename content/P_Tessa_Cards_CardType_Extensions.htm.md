# CardType.Extensions - свойство
Список расширений для типов карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public SealableObjectList<CardTypeExtension> Extensions { get; set; }
VB __Копировать
     Public Property Extensions As SealableObjectList(Of CardTypeExtension)
    	Get
    	Set
C++ __Копировать
     public:
    property SealableObjectList<CardTypeExtension^>^ Extensions {
    	SealableObjectList<CardTypeExtension^>^ get ();
    	void set (SealableObjectList<CardTypeExtension^>^ value);
    }
F# __Копировать
     member Extensions : SealableObjectList<CardTypeExtension> with get, set
#### Значение свойства
[SealableObjectList](T_Tessa_Platform_Collections_SealableObjectList_1.htm)<[CardTypeExtension](T_Tessa_Cards_CardTypeExtension.htm)>
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
