# CardType.CompletionOptions - свойство
Варианты завершения типа карточки задания.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public SealableObjectList<CardTypeCompletionOption> CompletionOptions { get; set; }
VB __Копировать
     Public Property CompletionOptions As SealableObjectList(Of CardTypeCompletionOption)
    	Get
    	Set
C++ __Копировать
     public:
    property SealableObjectList<CardTypeCompletionOption^>^ CompletionOptions {
    	SealableObjectList<CardTypeCompletionOption^>^ get ();
    	void set (SealableObjectList<CardTypeCompletionOption^>^ value);
    }
F# __Копировать
     member CompletionOptions : SealableObjectList<CardTypeCompletionOption> with get, set
#### Значение свойства
[SealableObjectList](T_Tessa_Platform_Collections_SealableObjectList_1.htm)<[CardTypeCompletionOption](T_Tessa_Cards_CardTypeCompletionOption.htm)>
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
