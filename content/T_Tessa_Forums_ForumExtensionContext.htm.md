# ForumExtensionContext - класс
Контекст выполнения запросов форумов
## __Definition
 **Пространство имён:** [Tessa.Forums](N_Tessa_Forums.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ForumExtensionContext : IForumExtensionContext
VB __Копировать
     Public NotInheritable Class ForumExtensionContext
    	Implements IForumExtensionContext
C++ __Копировать
     public ref class ForumExtensionContext sealed : IForumExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type ForumExtensionContext = 
        class
            interface IForumExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ForumExtensionContext
Implements
    [IForumExtensionContext](T_Tessa_Forums_IForumExtensionContext.htm)
##  __Конструкторы
[ForumExtensionContext](M_Tessa_Forums_ForumExtensionContext__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[CardContext](P_Tessa_Forums_ForumExtensionContext_CardContext.htm)|  Контекст
процесса взаимодействия с карточкой.  
---|---  
[Current](P_Tessa_Forums_ForumExtensionContext_Current.htm)|  Текущий контекст
[IForumExtensionContext](T_Tessa_Forums_IForumExtensionContext.htm).  
[HasCurrent](P_Tessa_Forums_ForumExtensionContext_HasCurrent.htm)|  Признак
того, что текущий код выполняется внутри операции с контекстом
[IForumExtensionContext](T_Tessa_Forums_IForumExtensionContext.htm), а
свойство [Current](P_Tessa_Forums_ForumExtensionContext_Current.htm) ссылается
на действительный контекст.  
[Unknown](P_Tessa_Forums_ForumExtensionContext_Unknown.htm)|  Неизвестный
контекст [IForumExtensionContext](T_Tessa_Forums_IForumExtensionContext.htm).  
## __Методы
[Create(ICardExtensionContext)](M_Tessa_Forums_ForumExtensionContext_Create.htm)|
Создаёт область операции, в которой заданный токен будет являться текущим в
контексте.  
---|---  
[Create(IForumExtensionContext)](M_Tessa_Forums_ForumExtensionContext_Create_1.htm)|
Создаёт область операции, в которой заданный контекст будет являться текущим.  
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
[Tessa.Forums - пространство имён](N_Tessa_Forums.htm)
