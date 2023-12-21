# CardResponseBase.EraseOnError - метод
Удаляет информацию из ответа на запрос, нежелательную для внешнего кода в
случае возникновения ошибки в момент после того, как информация была заполнена
(например, в расширениях AfterRequest).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual void EraseOnError()
VB __Копировать
     Public Overridable Sub EraseOnError
C++ __Копировать
     public:
    virtual void EraseOnError()
F# __Копировать
     abstract EraseOnError : unit -> unit 
    override EraseOnError : unit -> unit 
## __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[CardResponseBase - ](T_Tessa_Cards_CardResponseBase.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
