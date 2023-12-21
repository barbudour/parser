# NumberContext.Composer - свойство
Объект, обрабатывающий логику выделения и изменения номеров карточек. Если
объект недоступен или уже был установлен, то выбрасывается исключение
[System.InvalidOperationException].
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public INumberComposer Composer { get; set; }
VB __Копировать
     Public Property Composer As INumberComposer
    	Get
    	Set
C++ __Копировать
     public:
    virtual property INumberComposer^ Composer {
    	INumberComposer^ get () sealed;
    	void set (INumberComposer^ value) sealed;
    }
F# __Копировать
     abstract Composer : INumberComposer with get, set
    override Composer : INumberComposer with get, set
#### Значение свойства
[INumberComposer](T_Tessa_Cards_Numbers_INumberComposer.htm)
#### Реализации
[INumberContext.Composer](P_Tessa_Cards_Numbers_INumberContext_Composer.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[NumberContext - ](T_Tessa_Cards_Numbers_NumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
