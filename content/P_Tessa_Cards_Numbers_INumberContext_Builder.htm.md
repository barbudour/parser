# INumberContext.Builder - свойство
Объект, осуществляющий низкоуровневые действия с номерами, которые зависят от
бизнес-логики. Если объект недоступен или уже был установлен, то выбрасывается
исключение [System.InvalidOperationException].
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    INumberBuilder Builder { get; set; }
VB __Копировать
     Property Builder As INumberBuilder
    	Get
    	Set
C++ __Копировать
    property INumberBuilder^ Builder {
    	INumberBuilder^ get ();
    	void set (INumberBuilder^ value);
    }
F# __Копировать
     abstract Builder : INumberBuilder with get, set
#### Значение свойства
[INumberBuilder](T_Tessa_Cards_Numbers_INumberBuilder.htm)
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[INumberContext - ](T_Tessa_Cards_Numbers_INumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
