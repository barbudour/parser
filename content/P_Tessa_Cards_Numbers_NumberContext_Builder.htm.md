# NumberContext.Builder - свойство
Объект, осуществляющий низкоуровневые действия с номерами, которые зависят от
бизнес-логики. Если объект недоступен или уже был установлен, то выбрасывается
исключение [System.InvalidOperationException].
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public INumberBuilder Builder { get; set; }
VB __Копировать
     Public Property Builder As INumberBuilder
    	Get
    	Set
C++ __Копировать
     public:
    virtual property INumberBuilder^ Builder {
    	INumberBuilder^ get () sealed;
    	void set (INumberBuilder^ value) sealed;
    }
F# __Копировать
     abstract Builder : INumberBuilder with get, set
    override Builder : INumberBuilder with get, set
#### Значение свойства
[INumberBuilder](T_Tessa_Cards_Numbers_INumberBuilder.htm)
#### Реализации
[INumberContext.Builder](P_Tessa_Cards_Numbers_INumberContext_Builder.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[NumberContext - ](T_Tessa_Cards_Numbers_NumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
