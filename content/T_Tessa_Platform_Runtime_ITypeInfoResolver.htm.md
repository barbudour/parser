# ITypeInfoResolver - интерфейс
Объект, получающий информацию по типу карточки. Зарегистрирован в Unity только
в том случае, если зарегистрированы карточки.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ITypeInfoResolver
VB __Копировать
     Public Interface ITypeInfoResolver
C++ __Копировать
     public interface class ITypeInfoResolver
F# __Копировать
     type ITypeInfoResolver = interface end
##  __Методы
[TryGetCaptionAsync](M_Tessa_Platform_Runtime_ITypeInfoResolver_TryGetCaptionAsync.htm)|
Возвращает отображаемое имя типа карточки или null, если тип карточки не
найден. Возвращённое значение может быть строкой локализации.  
---|---  
[TryGetNameAsync](M_Tessa_Platform_Runtime_ITypeInfoResolver_TryGetNameAsync.htm)|
Возвращает имя типа карточки или null, если тип карточки не найден.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
