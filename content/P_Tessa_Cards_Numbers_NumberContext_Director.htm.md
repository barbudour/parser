# NumberContext.Director - свойство
Объект, управляющий взаимодействием с номерами карточек. Если объект
недоступен или уже был установлен, то выбрасывается исключение
[System.InvalidOperationException].
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public INumberDirectorBase Director { get; set; }
VB __Копировать
     Public Property Director As INumberDirectorBase
    	Get
    	Set
C++ __Копировать
     public:
    virtual property INumberDirectorBase^ Director {
    	INumberDirectorBase^ get () sealed;
    	void set (INumberDirectorBase^ value) sealed;
    }
F# __Копировать
     abstract Director : INumberDirectorBase with get, set
    override Director : INumberDirectorBase with get, set
#### Значение свойства
[INumberDirectorBase](T_Tessa_Cards_Numbers_INumberDirectorBase.htm)
#### Реализации
[INumberContext.Director](P_Tessa_Cards_Numbers_INumberContext_Director.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[NumberContext - ](T_Tessa_Cards_Numbers_NumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
