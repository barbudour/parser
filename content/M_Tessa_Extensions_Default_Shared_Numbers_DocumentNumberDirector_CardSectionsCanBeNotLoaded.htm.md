# DocumentNumberDirector.CardSectionsCanBeNotLoaded - метод
Признак того, что секции карточки, возможно, не загружены. Такая ситуация
возникает, в основном, при повторных сохранениях карточек или при удалении
карточек без возможности восстановления.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Numbers](N_Tessa_Extensions_Default_Shared_Numbers.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual bool CardSectionsCanBeNotLoaded(
    	INumberContext context
    )
VB __Копировать
     Protected Overridable Function CardSectionsCanBeNotLoaded ( 
    	context As INumberContext
    ) As Boolean
C++ __Копировать
     protected:
    virtual bool CardSectionsCanBeNotLoaded(
    	INumberContext^ context
    )
F# __Копировать
     abstract CardSectionsCanBeNotLoaded : 
            context : INumberContext -> bool 
    override CardSectionsCanBeNotLoaded : 
            context : INumberContext -> bool 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если секции карточки могут быть не загружены; false в противном случае.
## __См. также
#### Ссылки
[DocumentNumberDirector -
](T_Tessa_Extensions_Default_Shared_Numbers_DocumentNumberDirector.htm)
[Tessa.Extensions.Default.Shared.Numbers - пространство
имён](N_Tessa_Extensions_Default_Shared_Numbers.htm)
