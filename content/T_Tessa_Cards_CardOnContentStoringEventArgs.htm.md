# CardOnContentStoringEventArgs - класс
Аргументы события
[OnContentStoring](E_Tessa_Cards_Extensions_ICardStoreExtensionContext_OnContentStoring.htm),
вызываемого перед сохранением содержимого каждого из файлов.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardOnContentStoringEventArgs : DeferredEventArgs
VB __Копировать
     Public NotInheritable Class CardOnContentStoringEventArgs
    	Inherits DeferredEventArgs
C++ __Копировать
     public ref class CardOnContentStoringEventArgs sealed : public DeferredEventArgs
F# __Копировать
     [<SealedAttribute>]
    type CardOnContentStoringEventArgs = 
        class
            inherit DeferredEventArgs
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[EventArgs](https://learn.microsoft.com/dotnet/api/system.eventargs) __[DeferredEventArgs](T_Tessa_Platform_DeferredEventArgs.htm) __ CardOnContentStoringEventArgs
##  __Конструкторы
[CardOnContentStoringEventArgs(ICardStoreExtensionContext)](M_Tessa_Cards_CardOnContentStoringEventArgs__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
[CardOnContentStoringEventArgs(ICardStoreExtensionContext, CardContentContext,
Stream)](M_Tessa_Cards_CardOnContentStoringEventArgs__ctor_1.htm)|
Инициализирует новый экземпляр класса CardOnContentStoringEventArgs  
##  __Свойства
[Cancel](P_Tessa_Cards_CardOnContentStoringEventArgs_Cancel.htm)|  Установка
данного флага отменяет стандартное сохранение контента файла в платформе.
Данный флаг следует использовать только в ситуации, когда файл сохраняется в
расширении, иначе в карточке будут файлы, которые не имеют контента.  
---|---  
[CancellationToken](P_Tessa_Cards_CardOnContentStoringEventArgs_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
[ContentContext](P_Tessa_Cards_CardOnContentStoringEventArgs_ContentContext.htm)|
Контекст сохранения контента файла.  
[ContentStream](P_Tessa_Cards_CardOnContentStoringEventArgs_ContentStream.htm)|
Поток с контентом файла. Можно переопределить для сохранения другого или
модифицированного файла.  
[Context](P_Tessa_Cards_CardOnContentStoringEventArgs_Context.htm)|  Контекст
расширений на сохранение карточки.  
[Success](P_Tessa_Cards_CardOnContentStoringEventArgs_Success.htm)|  Признак
того, что карточка была успешно сохранена, все расширения успешно выполнены (в
т.ч. AfterRequest), после чего успешно сохранено содержимое всех файлов.
Соответствует признаку того, что результат успешен
Context.ValidationResult.IsSuccessful() на момент вызова обработчиков событий
[ContentStoreCompleted](E_Tessa_Cards_Extensions_ICardStoreExtensionContext_ContentStoreCompleted.htm).  
## __Методы
[Defer](M_Tessa_Platform_DeferredEventArgs_Defer.htm)|  Возвращает объект,
обеспечивающий ожидание действия. Вызовите метод в блоке using, внутри
которого выполняйте любые ожидания await.  
(Унаследован от [DeferredEventArgs](T_Tessa_Platform_DeferredEventArgs.htm))  
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
[IsPropertyChanged](M_Tessa_UI_Controls_PropertyChangedHelper_IsPropertyChanged.htm)|
Проверяет наступление события изменения свойства propertyName  
(Определяется
[PropertyChangedHelper](T_Tessa_UI_Controls_PropertyChangedHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
