# NumberContext.RequestRepository - свойство
Репозиторий, используемый для построения универсальных запросов к API номеров
на сервере.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ICardRepository RequestRepository { get; }
VB __Копировать
     Public ReadOnly Property RequestRepository As ICardRepository
    	Get
C++ __Копировать
     public:
    virtual property ICardRepository^ RequestRepository {
    	ICardRepository^ get () sealed;
    }
F# __Копировать
     abstract RequestRepository : ICardRepository with get
    override RequestRepository : ICardRepository with get
#### Значение свойства
[ICardRepository](T_Tessa_Cards_ICardRepository.htm)
#### Реализации
[INumberDependencies.RequestRepository](P_Tessa_Cards_Numbers_INumberDependencies_RequestRepository.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[NumberContext - ](T_Tessa_Cards_Numbers_NumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
