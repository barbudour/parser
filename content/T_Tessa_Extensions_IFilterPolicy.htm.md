# IFilterPolicy - интерфейс
Политика, определяющая фильтр для выполнения метода расширения.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFilterPolicy : IExtensionPolicy
VB __Копировать
     Public Interface IFilterPolicy
    	Inherits IExtensionPolicy
C++ __Копировать
     public interface class IFilterPolicy : IExtensionPolicy
F# __Копировать
     type IFilterPolicy = 
        interface
            interface IExtensionPolicy
        end
Implements
    [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm)
##  __Методы
[FilterAsync](M_Tessa_Extensions_IFilterPolicy_FilterAsync.htm)|  Возвращает
признак того, что выполнение метода с заданным параметром разрешено для
экземпляра расширения.  
---|---  
[GetFilterContextAsync](M_Tessa_Extensions_IFilterPolicy_GetFilterContextAsync.htm)|
Возвращает контекст фильтрации, используемый для определение разрешений на
выполнение метода для экземпляров расширений.  
## __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
