# CardLibrary.Items - свойство
Список записей в библиотеке с карточками.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public SealableObjectList<CardLibraryItem> Items { get; set; }
VB __Копировать
     Public Property Items As SealableObjectList(Of CardLibraryItem)
    	Get
    	Set
C++ __Копировать
     public:
    property SealableObjectList<CardLibraryItem^>^ Items {
    	SealableObjectList<CardLibraryItem^>^ get ();
    	void set (SealableObjectList<CardLibraryItem^>^ value);
    }
F# __Копировать
     member Items : SealableObjectList<CardLibraryItem> with get, set
#### Значение свойства
[SealableObjectList](T_Tessa_Platform_Collections_SealableObjectList_1.htm)<[CardLibraryItem](T_Tessa_Cards_CardLibraryItem.htm)>
##  __Заметки
Значение свойства никогда не равно null.
## __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardLibrary - ](T_Tessa_Cards_CardLibrary.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
