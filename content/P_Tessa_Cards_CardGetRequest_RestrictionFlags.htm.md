# CardGetRequest.RestrictionFlags - свойство
Флаги, ограничивающие загружаемую по карточке информацию. По умолчанию
загружаемая информация не ограничивается.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardGetRestrictionFlags RestrictionFlags { get; set; }
VB __Копировать
     Public Property RestrictionFlags As CardGetRestrictionFlags
    	Get
    	Set
C++ __Копировать
     public:
    property CardGetRestrictionFlags RestrictionFlags {
    	CardGetRestrictionFlags get ();
    	void set (CardGetRestrictionFlags value);
    }
F# __Копировать
     member RestrictionFlags : CardGetRestrictionFlags with get, set
#### Значение свойства
[CardGetRestrictionFlags](T_Tessa_Cards_CardGetRestrictionFlags.htm)
##  __Заметки
Значение по умолчанию [None](T_Tessa_Cards_CardGetRestrictionFlags.htm)
возвращается даже в том случае, если объект с соответствующим ключом
отсутствует в хранилище.
## __См. также
#### Ссылки
[CardGetRequest - ](T_Tessa_Cards_CardGetRequest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
