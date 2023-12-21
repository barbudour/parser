# CardTypeCompletionOption.Validators - свойство
Список валидаторов, используемых для варианта завершения.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public SealableObjectList<CardTypeValidator> Validators { get; set; }
VB __Копировать
     Public Property Validators As SealableObjectList(Of CardTypeValidator)
    	Get
    	Set
C++ __Копировать
     public:
    property SealableObjectList<CardTypeValidator^>^ Validators {
    	SealableObjectList<CardTypeValidator^>^ get ();
    	void set (SealableObjectList<CardTypeValidator^>^ value);
    }
F# __Копировать
     member Validators : SealableObjectList<CardTypeValidator> with get, set
#### Значение свойства
[SealableObjectList](T_Tessa_Platform_Collections_SealableObjectList_1.htm)<[CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm)>
##  __Заметки
Значение свойства никогда не равно null.
## __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardTypeCompletionOption - ](T_Tessa_Cards_CardTypeCompletionOption.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
