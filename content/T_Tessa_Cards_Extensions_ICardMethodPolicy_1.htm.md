# ICardMethodPolicy<TMethod> \- интерфейс
Политика, проверяющая допустимость метода выполнения запроса к API карточек
для расширений.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardMethodPolicy<in TMethod> : IExtensionPolicy
    where TMethod : struct, new()
VB __Копировать
     Public Interface ICardMethodPolicy(Of In TMethod As {Structure, New})
    	Inherits IExtensionPolicy
C++ __Копировать
    generic<typename TMethod>
    where TMethod : value class, gcnew()
    public interface class ICardMethodPolicy : IExtensionPolicy
F# __Копировать
     type ICardMethodPolicy<'TMethod when 'TMethod : struct, new()> = 
        interface
            interface IExtensionPolicy
        end
Implements
    [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm)
#### Параметры типа
TMethod
    Тип метода выполнения запроса к API карточек.
##  __Методы
[IsAllowed](M_Tessa_Cards_Extensions_ICardMethodPolicy_1_IsAllowed.htm)|
Проверяет, что заданный метод является допустимым для выполнения расширения.  
---|---  
##  __См. также
#### Ссылки
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
