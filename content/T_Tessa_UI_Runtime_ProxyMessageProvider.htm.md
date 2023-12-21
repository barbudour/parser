# ProxyMessageProvider - класс
Объект, обеспечивающий вывод сообщений средствами основного или прокси
провайдера.
## __Definition
 **Пространство имён:** [Tessa.UI.Runtime](N_Tessa_UI_Runtime.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ProxyMessageProvider : IMessageProvider
VB __Копировать
     Public NotInheritable Class ProxyMessageProvider
    	Implements IMessageProvider
C++ __Копировать
     public ref class ProxyMessageProvider sealed : IMessageProvider
F# __Копировать
     [<SealedAttribute>]
    type ProxyMessageProvider = 
        class
            interface IMessageProvider
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ProxyMessageProvider
Implements
    [IMessageProvider](T_Tessa_Platform_Runtime_IMessageProvider.htm)
##  __Заметки
Терминология основной-прокси условная.
## __Конструкторы
[ProxyMessageProvider](M_Tessa_UI_Runtime_ProxyMessageProvider__ctor.htm)|
Конструктор.  
---|---  
## __Свойства
[UseProxyProvider](P_Tessa_UI_Runtime_ProxyMessageProvider_UseProxyProvider.htm)|
Признак использования прокси провайдера сообщений.  
---|---  
## __Методы
[ConfirmAsync](M_Tessa_UI_Runtime_ProxyMessageProvider_ConfirmAsync.htm)|
Выводит заданное сообщение и ожидает ответа да/нет. Возвращает признак того,
что пользователь выбрал "да".  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ShowExceptionAsync](M_Tessa_UI_Runtime_ProxyMessageProvider_ShowExceptionAsync.htm)|
Выводит информацию по исключению.  
[ShowNotEmptyAsync](M_Tessa_UI_Runtime_ProxyMessageProvider_ShowNotEmptyAsync.htm)|
Выводит сообщение с результатом валидации, если он не пустой.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.UI.Runtime - пространство имён](N_Tessa_UI_Runtime.htm)
