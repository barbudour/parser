# ExtensionContainer.InvalidateRegulation<TExtension> \- метод
Принудительно устанавливает необходимость повторного выполнения этапа
упорядочивания для заданного типа расширения. Вызывать метод не требуется в
случае, если была повторно зарегистрирована стратегия инициализации или
упорядочивания, или если для заданного типа расширения была выполнена
регистрация типа экземпляра расширения.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void InvalidateRegulation<TExtension>()
    where TExtension : class, IExtension
VB __Копировать
     Public Sub InvalidateRegulation(Of TExtension As {Class, IExtension})
C++ __Копировать
     public:
    generic<typename TExtension>
    where TExtension : ref class, IExtension
    virtual void InvalidateRegulation() sealed
F# __Копировать
     abstract InvalidateRegulation : unit -> unit  when 'TExtension : not struct and IExtension
    override InvalidateRegulation : unit -> unit  when 'TExtension : not struct and IExtension
#### Параметры типа
TExtension
    Тип расширения.
#### Реализации
[IExtensionContainer.InvalidateRegulation<TExtension>()](M_Tessa_Extensions_IExtensionContainer_InvalidateRegulation__1.htm)  
##  __См. также
#### Ссылки
[ExtensionContainer - ](T_Tessa_Extensions_ExtensionContainer.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
