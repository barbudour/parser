# CardDeleteRequest.DeletionMode - свойство
Способ удаления карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardDeletionMode DeletionMode { get; set; }
VB __Копировать
     Public Property DeletionMode As CardDeletionMode
    	Get
    	Set
C++ __Копировать
     public:
    property CardDeletionMode DeletionMode {
    	CardDeletionMode get ();
    	void set (CardDeletionMode value);
    }
F# __Копировать
     member DeletionMode : CardDeletionMode with get, set
#### Значение свойства
[CardDeletionMode](T_Tessa_Cards_CardDeletionMode.htm)
##  __Заметки
Значение по умолчанию WithoutBackup возвращает даже в том случае, если элемент
отсутствовал в хранилище.
## __См. также
#### Ссылки
[CardDeleteRequest - ](T_Tessa_Cards_CardDeleteRequest.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
