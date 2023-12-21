# INumberContext.Composer - свойство
Объект, обрабатывающий логику выделения и изменения номеров карточек. Если
объект недоступен или уже был установлен, то выбрасывается исключение
[System.InvalidOperationException].
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    INumberComposer Composer { get; set; }
VB __Копировать
     Property Composer As INumberComposer
    	Get
    	Set
C++ __Копировать
    property INumberComposer^ Composer {
    	INumberComposer^ get ();
    	void set (INumberComposer^ value);
    }
F# __Копировать
     abstract Composer : INumberComposer with get, set
#### Значение свойства
[INumberComposer](T_Tessa_Cards_Numbers_INumberComposer.htm)
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[INumberContext - ](T_Tessa_Cards_Numbers_INumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
