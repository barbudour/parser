# KrCardMetadataExtensionBase.GetAllSectionsAsync - метод
Получить все секции метаданных о таблицах.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract ValueTask<CardMetadataSectionCollection> GetAllSectionsAsync(
    	ICardMetadataExtensionContext context
    )
VB __Копировать
     Protected MustOverride Function GetAllSectionsAsync ( 
    	context As ICardMetadataExtensionContext
    ) As ValueTask(Of CardMetadataSectionCollection)
C++ __Копировать
     protected:
    virtual ValueTask<CardMetadataSectionCollection^> GetAllSectionsAsync(
    	ICardMetadataExtensionContext^ context
    ) abstract
F# __Копировать
     abstract GetAllSectionsAsync : 
            context : ICardMetadataExtensionContext -> ValueTask<CardMetadataSectionCollection> 
#### Параметры
context
[ICardMetadataExtensionContext](T_Tessa_Cards_Extensions_ICardMetadataExtensionContext.htm)
    Контекст выполнения операции, предоставляющий доступ к метаданным.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardMetadataSectionCollection](T_Tessa_Cards_Metadata_CardMetadataSectionCollection.htm)>  
Коллекция секций метаданных о таблицах.
##  __См. также
#### Ссылки
[KrCardMetadataExtensionBase -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCardMetadataExtensionBase.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
